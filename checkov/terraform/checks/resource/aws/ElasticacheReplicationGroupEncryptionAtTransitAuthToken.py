from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class ElasticacheReplicationGroupEncryptionAtTransitAuthToken(BaseResourceCheck):
    def __init__(self):
        name = "Ensure all data stored in the Elasticache Replication Group is securely encrypted at transit and has auth token"
        id = "CKV_AWS_31"
        supported_resources = ['aws_elasticache_replication_group']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for encryption configuration at aws_elasticache_replication_group:
            https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html
        :param conf: aws_elasticache_replication_group configuration
        :return: <CheckResult>
        """
        self.evaluated_keys = ['transit_encryption_enabled', 'auth_token']
        if "transit_encryption_enabled" in conf.keys():
            if conf["transit_encryption_enabled"][0]:
                if "auth_token" in conf.keys():
                    return CheckResult.PASSED
        return CheckResult.FAILED


check = ElasticacheReplicationGroupEncryptionAtTransitAuthToken()
