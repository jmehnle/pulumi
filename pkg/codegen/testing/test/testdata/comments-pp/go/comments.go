package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		securityGroup, err := ec2.NewSecurityGroup(ctx, "securityGroup", &ec2.SecurityGroupArgs{
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					Protocol: pulumi.String("tcp"),
					FromPort: pulumi.Int(0),
					ToPort:   pulumi.Int(0),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
				},
			},
		})
		if err != nil {
			return err
		}
		ami, err := aws.GetAmi(ctx, &aws.GetAmiArgs{
			Filters: []aws.GetAmiFilter{
				{
					Name: "name",
					Values: []string{
						"amzn-ami-hvm-*-x86_64-ebs",
					},
				},
			},
			Owners: []string{
				"137112412989",
			},
			MostRecent: pulumi.BoolRef(true),
		}, nil)
		if err != nil {
			return err
		}
		_, err = ec2.NewInstance(ctx, "server", &ec2.InstanceArgs{
			Tags: pulumi.StringMap{
				"Name": pulumi.String("web-server-www"),
			},
			InstanceType: pulumi.String("t2.micro"),
			SecurityGroups: pulumi.StringArray{
				securityGroup.Name,
			},
			Ami:      pulumi.String(ami.Id),
			UserData: pulumi.String(fmt.Sprintf("#!/bin/bash\necho \"Hello, World!\" > index.html\nnohup python -m SimpleHTTPServer 80 &\n")),
		})
		if err != nil {
			return err
		}
		ctx.Export("secGroupName", securityGroup.Name)
		return nil
	})
}