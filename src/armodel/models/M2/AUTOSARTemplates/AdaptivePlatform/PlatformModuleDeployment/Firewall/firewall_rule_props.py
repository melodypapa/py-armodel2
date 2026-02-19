"""FirewallRuleProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule import (
    FirewallRule,
)


class FirewallRuleProps(ARObject):
    """AUTOSAR FirewallRuleProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    action: Optional[Any]
    matching_egresses: list[FirewallRule]
    matchings: list[FirewallRule]
    def __init__(self) -> None:
        """Initialize FirewallRuleProps."""
        super().__init__()
        self.action: Optional[Any] = None
        self.matching_egresses: list[FirewallRule] = []
        self.matchings: list[FirewallRule] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRuleProps":
        """Deserialize XML element to FirewallRuleProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FirewallRuleProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse action
        child = ARObject._find_child_element(element, "ACTION")
        if child is not None:
            action_value = child.text
            obj.action = action_value

        # Parse matching_egresses (list from container "MATCHING-EGRESSES")
        obj.matching_egresses = []
        container = ARObject._find_child_element(element, "MATCHING-EGRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.matching_egresses.append(child_value)

        # Parse matchings (list from container "MATCHINGS")
        obj.matchings = []
        container = ARObject._find_child_element(element, "MATCHINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.matchings.append(child_value)

        return obj



class FirewallRulePropsBuilder:
    """Builder for FirewallRuleProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FirewallRuleProps = FirewallRuleProps()

    def build(self) -> FirewallRuleProps:
        """Build and return FirewallRuleProps object.

        Returns:
            FirewallRuleProps instance
        """
        # TODO: Add validation
        return self._obj
