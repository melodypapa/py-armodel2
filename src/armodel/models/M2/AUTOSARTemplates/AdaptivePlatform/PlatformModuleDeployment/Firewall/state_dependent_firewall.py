"""StateDependentFirewall AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 583)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule_props import (
    FirewallRuleProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class StateDependentFirewall(ARElement):
    """AUTOSAR StateDependentFirewall."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_action: Optional[Any]
    firewall_rule_propses: list[FirewallRuleProps]
    firewall_states: list[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize StateDependentFirewall."""
        super().__init__()
        self.default_action: Optional[Any] = None
        self.firewall_rule_propses: list[FirewallRuleProps] = []
        self.firewall_states: list[ModeDeclaration] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "StateDependentFirewall":
        """Deserialize XML element to StateDependentFirewall object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StateDependentFirewall object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StateDependentFirewall, cls).deserialize(element)

        # Parse default_action
        child = ARObject._find_child_element(element, "DEFAULT-ACTION")
        if child is not None:
            default_action_value = child.text
            obj.default_action = default_action_value

        # Parse firewall_rule_propses (list from container "FIREWALL-RULE-PROPSES")
        obj.firewall_rule_propses = []
        container = ARObject._find_child_element(element, "FIREWALL-RULE-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.firewall_rule_propses.append(child_value)

        # Parse firewall_states (list from container "FIREWALL-STATES")
        obj.firewall_states = []
        container = ARObject._find_child_element(element, "FIREWALL-STATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.firewall_states.append(child_value)

        return obj



class StateDependentFirewallBuilder:
    """Builder for StateDependentFirewall."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StateDependentFirewall = StateDependentFirewall()

    def build(self) -> StateDependentFirewall:
        """Build and return StateDependentFirewall object.

        Returns:
            StateDependentFirewall instance
        """
        # TODO: Add validation
        return self._obj
