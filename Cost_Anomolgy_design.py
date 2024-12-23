from diagrams import Diagram, Cluster, Node
from diagrams.aws.management import OrganizationsAccount, Organizations, ControlTower, Cloudwatch
from diagrams.aws.integration import SNS
from diagrams.aws.compute import Lambda
from diagrams.aws.cost import CostAndUsageReport, CostExplorer
from diagrams.aws.security import Shield
from diagrams.custom import Custom

# Define a custom node for QuickSight
class QuickSight(Node):
    _provider = "aws"
    _type = "analytics"
    _icon_dir = "resources"

    def __init__(self, label: str = "QuickSight Dashboards"):
        super().__init__(label)


# Set diagram attributes with horizontal layout for clarity
with Diagram("AWS Control Tower Cost Monitoring Architecture", show=False, direction="LR"):
    # Main AWS Cluster
    with Cluster("AWS"):
        # Management Components
        with Cluster("Management"):
            control_tower = ControlTower("Control Tower")
            org = Organizations("Organizations")
        
        # Organization Units (Adjusted for layout without width)
        with Cluster("Organization Units"):
            with Cluster("Development OU"):  # Broader Development OU
                dev_accounts = [OrganizationsAccount("Dev Account 1"),
                                OrganizationsAccount("Dev Account 2")]
            
            with Cluster("Test OU"):  # Broader Test OU
                test_accounts = [OrganizationsAccount("Test Account 1"),
                                 OrganizationsAccount("Test Account 2")]
            
            with Cluster("Production OU"):  # Broader Production OU
                prod_accounts = [OrganizationsAccount("Prod Account 1"),
                                 OrganizationsAccount("Prod Account 2")]
        
        # Cost Management Services
        with Cluster("Cost Management"):
            cur = CostAndUsageReport("Cost & Usage Reports")
            cost_explorer = CostExplorer("Cost Explorer")
            cost_anomaly = Shield("Cost Anomaly Detection")
        
        # Monitoring & Alerting
        with Cluster("Monitoring & Alerting"):
            sns = SNS("SNS Topics")
            lambda_fn = Lambda("Lambda Functions")
            cloudwatch = Cloudwatch("CloudWatch")
        
        # Visualization
        with Cluster("Visualization"):
            quicksight = QuickSight("QuickSight Dashboards")
    
    # Define relationships
    control_tower >> org
    
    # Connect OUs to org
    org >> dev_accounts
    org >> test_accounts
    org >> prod_accounts
    
    # Cost data flow
    dev_accounts >> cur
    test_accounts >> cur
    prod_accounts >> cur
    
    cur >> cost_explorer
    cur >> cost_anomaly
    
    # Alerting flow
    cost_anomaly >> sns
    cost_explorer >> sns
    sns >> lambda_fn
    lambda_fn >> cloudwatch
    
    # Visualization flow
    cur >> quicksight
    cost_explorer >> quicksight
    cost_anomaly >> quicksight
