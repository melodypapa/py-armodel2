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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    firewall_state_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize StateDependentFirewall."""
        super().__init__()
        self.default_action: Optional[Any] = None
        self.firewall_rule_propses: list[FirewallRuleProps] = []
        self.firewall_state_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize StateDependentFirewall to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StateDependentFirewall, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_action
        if self.default_action is not None:
            serialized = SerializationHelper.serialize_item(self.default_action, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize firewall_rule_propses (list to container "FIREWALL-RULE-PROPSES")
        if self.firewall_rule_propses:
            wrapper = ET.Element("FIREWALL-RULE-PROPSES")
            for item in self.firewall_rule_propses:
                serialized = SerializationHelper.serialize_item(item, "FirewallRuleProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize firewall_state_refs (list to container "FIREWALL-STATE-REFS")
        if self.firewall_state_refs:
            wrapper = ET.Element("FIREWALL-STATE-REFS")
            for item in self.firewall_state_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    child_elem = ET.Element("FIREWALL-STATE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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
        child = SerializationHelper.find_child_element(element, "DEFAULT-ACTION")
        if child is not None:
            default_action_value = child.text
            obj.default_action = default_action_value

        # Parse firewall_rule_propses (list from container "FIREWALL-RULE-PROPSES")
        obj.firewall_rule_propses = []
        container = SerializationHelper.find_child_element(element, "FIREWALL-RULE-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.firewall_rule_propses.append(child_value)

        # Parse firewall_state_refs (list from container "FIREWALL-STATE-REFS")
        obj.firewall_state_refs = []
        container = SerializationHelper.find_child_element(element, "FIREWALL-STATE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.firewall_state_refs.append(child_value)

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
