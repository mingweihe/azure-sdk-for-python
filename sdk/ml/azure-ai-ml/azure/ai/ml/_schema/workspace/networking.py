# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from marshmallow import fields, post_load

from azure.ai.ml._schema.core.fields import NestedField
from azure.ai.ml._schema.core.schema_meta import PatchedSchemaMeta
from azure.ai.ml.entities import Networking, NetworkRuleMeta

class NetworkRuleMetaSchema(metaclass=PatchedSchemaMeta):
    direction: fields.Str(required=False)
    type: fields.Str(required=False)
    destination: fields.Str(required=False)

    @post_load
    def make(self, data, **kwargs):
        return NetworkRuleMeta(data)


class NetworingSchema(metaclass=PatchedSchemaMeta):
    managed_network_isolation: fields.Str(required=False)
    outbound_rule: fields.Dict(
        keys=fields.Str(required=True), values=NestedField(NetworkRuleMetaSchema, allow_none=True), allow_none=True
    )

    @post_load
    def make(self, data, **kwargs):
        return Networking(data)
