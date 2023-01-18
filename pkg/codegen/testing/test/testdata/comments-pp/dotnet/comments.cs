using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() => 
{
    // Test comments for a resource
    var securityGroup = new Aws.Ec2.SecurityGroup("securityGroup", new()
    {
        Ingress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupIngressArgs
            {
                Protocol = "tcp",
                FromPort = 0,
                ToPort = 0,
                CidrBlocks = new[]
                {
                    "0.0.0.0/0",
                },
            },
        },
    });

    var ami = Aws.GetAmi.Invoke(new()
    {
        Filters = new[]
        {
            new Aws.Inputs.GetAmiFilterInputArgs
            {
                Name = "name",
                Values = new[]
                {
                    "amzn-ami-hvm-*-x86_64-ebs",
                },
            },
        },
        Owners = new[]
        {
            "137112412989",
        },
        MostRecent = true,
    });

    // Test comments for another resource
    var server = new Aws.Ec2.Instance("server", new()
    {
        Tags = 
        {
            { "Name", "web-server-www" },
        },
        InstanceType = "t2.micro",
        SecurityGroups = new[]
        {
            securityGroup.Name,
        },
        Ami = ami.Apply(getAmiResult => getAmiResult.Id),
        UserData = @"#!/bin/bash
echo ""Hello, World!"" > index.html
nohup python -m SimpleHTTPServer 80 &
",
    });

    // Final trailing resource comment
    return new Dictionary<string, object?>
    {
        ["secGroupName"] = securityGroup.Name,
    };
});
