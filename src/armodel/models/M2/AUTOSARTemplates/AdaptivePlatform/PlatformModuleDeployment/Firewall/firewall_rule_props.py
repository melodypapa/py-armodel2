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
    def serialize(self) -> ET.Element:
        """Serialize FirewallRuleProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize action
        if self.action is not None:
            serialized = ARObject._serialize_item(self.action, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize matching_egresses (list to container "MATCHING-EGRESSES")
        if self.matching_egresses:
            wrapper = ET.Element("MATCHING-EGRESSES")
            for item in self.matching_egresses:
                serialized = ARObject._serialize_item(item, "FirewallRule")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize matchings (list to container "MATCHINGS")
        if self.matchings:
            wrapper = ET.Element("MATCHINGS")
            for item in self.matchings:
                serialized = ARObject._serialize_item(item, "FirewallRule")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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
