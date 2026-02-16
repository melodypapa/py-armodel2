"""DoIpRoutingActivation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_targets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpLogicTargetAddressProps,
        ),  # doIpTargets
    }

    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_targets: list[DoIpLogicTargetAddressProps] = []


class DoIpRoutingActivationBuilder:
    """Builder for DoIpRoutingActivation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivation = DoIpRoutingActivation()

    def build(self) -> DoIpRoutingActivation:
        """Build and return DoIpRoutingActivation object.

        Returns:
            DoIpRoutingActivation instance
        """
        # TODO: Add validation
        return self._obj
