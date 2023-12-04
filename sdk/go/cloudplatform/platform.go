package cloudplatform

type AutomationJobArgs struct {
	Repo           string
	Dir            string
	PreRunCommands []string
	Entrypoint     string
	Environemnt    []string
	Mode           string
	Schedule       string
}

type Platform interface {
	CreateAutomationJob(name string, args AutomationJobArgs)
	Search(query string) ([]Resource, error)
	RunDeployment(args DeploymentArgs)
	GetServiceTemplate(name string) ServiceTemplate
}

type CloudPlatform struct{}

func NewCloudPlatform(org string) (Platform, error) {

	return &CloudPlatform{}, nil
}

func (c *CloudPlatform) CreateAutomationJob(name string, args AutomationJobArgs) {
	// TODO
}

func (c *CloudPlatform) RunDeployment(args DeploymentArgs)

func (c *CloudPlatform) Search(query string) ([]Resource, error) {
	// hit the pulumi cloud resource search API
	return nil, nil
}

func (c *CloudPlatform) GetServiceTemplate(name string) ServiceTemplate {
	return &CloudServiceTemplate{}
}

type Stack interface {
	SupportsDeployments() bool
	RunDeployment(args DeploymentArgs)
}

type CloudStack struct{}

func NewCloudStack() (Stack, error) {
	return &CloudStack{}, nil
}

type DeploymentArgs struct {
	Repo      string
	Operation string
	Dir       string
	EnvVars   []string
	Targets   []string
}

func (cs *CloudStack) SupportsDeployments() bool {
	return true
}

func (cs *CloudStack) RunDeployment(args DeploymentArgs) {
}

type Resource interface {
	Stack() Stack
	ID() string
	ReportPolicyViolation(Level string, Note string, RevalidationQuery string)
}

type CloudResource struct{}

func NewCloudResource() (Resource, error) {
	return &CloudResource{}, nil
}

func (cr *CloudResource) Stack() Stack {
	c, _ := NewCloudStack()
	return c
}

func (cr *CloudResource) ID() string {
	return ""
}

func (cr *CloudResource) ReportPolicyViolation(Level string, Note string, RevalidationQuery string) {
	// these APIs don't yet exist in pulumi cloud but you could imagine
	// a database of:
	// 	1. resource ID
	//  2. violation level
	// 	3. note
	//  4. revalition query (search query to check that resource is back in compliance)
	// would very very useful for rolling out broad new policy over existing infra
	// as well as policy on resources not managed by IaC but imported into Pulumi
}

type ServiceTemplate interface {
	TemplateAndDeploy(args TemplateArgs)
}

type CloudServiceTemplate struct{}

type TemplateArgs struct {
	DestinationRepo string
	Dir             string
	PushToDeploy    bool
	PRPreview       bool
	ReviewStacks    bool
	Drift           bool
	TTLSeconds      int64
	Environment     []string
}

func NewCloudServiceTemplate() ServiceTemplate {
	return &CloudServiceTemplate{}
}

func (cst *CloudServiceTemplate) TemplateAndDeploy(args TemplateArgs) {}
