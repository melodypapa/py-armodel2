"""FirewallRuleProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    matching_egresse_refs: list[ARRef]
    matching_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FirewallRuleProps."""
        super().__init__()
        self.action: Optional[Any] = None
        self.matching_egresse_refs: list[ARRef] = []
        self.matching_refs: list[ARRef] = []

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

        # Serialize matching_egresse_refs (list to container "MATCHING-EGRESSE-REFS")
        if self.matching_egresse_refs:
            wrapper = ET.Element("MATCHING-EGRESSE-REFS")
            for item in self.matching_egresse_refs:
                serialized = ARObject._serialize_item(item, "FirewallRule")
                if serialized is not None:
                    child_elem = ET.Element("MATCHING-EGRESSE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize matching_refs (list to container "MATCHING-REFS")
        if self.matching_refs:
            wrapper = ET.Element("MATCHING-REFS")
            for item in self.matching_refs:
                serialized = ARObject._serialize_item(item, "FirewallRule")
                if serialized is not None:
                    child_elem = ET.Element("MATCHING-REF")
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

        # Parse matching_egresse_refs (list from container "MATCHING-EGRESSE-REFS")
        obj.matching_egresse_refs = []
        container = ARObject._find_child_element(element, "MATCHING-EGRESSE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.matching_egresse_refs.append(child_value)

        # Parse matching_refs (list from container "MATCHING-REFS")
        obj.matching_refs = []
        container = ARObject._find_child_element(element, "MATCHING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.matching_refs.append(child_value)

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
