# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import Any, Dict, Optional

class NetworkRuleMeta:
    def __init__(
        self,
        *,
        direction: str = None,
        type: str = None,
        destination: str = None
    ) -> None:
        self.direction = direction
        self.type = type
        self.destination = destination

    @classmethod
    def _from_rest_object(cls, rest_obj: Any) -> "NetworkRuleMeta":
        return Networking()


class Networking:
    def __init__(
        self,
        *,
        managed_network_isolation: str = None,
        outbound_rule: Optional[Dict[str, NetworkRuleMeta]] = None
    ) -> None:
        self.managed_network_isolation = managed_network_isolation
        self.outbound_rule = outbound_rule

    @classmethod
    def _from_rest_object(cls, rest_obj: Any) -> "Networking":
        return Networking()
