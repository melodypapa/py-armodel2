"""FirewallRuleProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    action: Optional[FirewallActionEnum]
    matching_egress_rule_refs: list[ARRef]
    matching_ingress_rule_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FirewallRuleProps."""
        super().__init__()
        self.action: Optional[FirewallActionEnum] = None
        self.matching_egress_rule_refs: list[ARRef] = []
        self.matching_ingress_rule_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FirewallRuleProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FirewallRuleProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize action
        if self.action is not None:
            serialized = SerializationHelper.serialize_item(self.action, "FirewallActionEnum")
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

        # Serialize matching_egress_rule_refs (list to container "MATCHING-EGRESS-RULE-REFS")
        if self.matching_egress_rule_refs:
            wrapper = ET.Element("MATCHING-EGRESS-RULE-REFS")
            for item in self.matching_egress_rule_refs:
                serialized = SerializationHelper.serialize_item(item, "FirewallRule")
                if serialized is not None:
                    child_elem = ET.Element("MATCHING-EGRESS-RULE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize matching_ingress_rule_refs (list to container "MATCHING-INGRESS-RULE-REFS")
        if self.matching_ingress_rule_refs:
            wrapper = ET.Element("MATCHING-INGRESS-RULE-REFS")
            for item in self.matching_ingress_rule_refs:
                serialized = SerializationHelper.serialize_item(item, "FirewallRule")
                if serialized is not None:
                    child_elem = ET.Element("MATCHING-INGRESS-RULE-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FirewallRuleProps, cls).deserialize(element)

        # Parse action
        child = SerializationHelper.find_child_element(element, "ACTION")
        if child is not None:
            action_value = SerializationHelper.deserialize_by_tag(child, "FirewallActionEnum")
            obj.action = action_value

        # Parse matching_egress_rule_refs (list from container "MATCHING-EGRESS-RULE-REFS")
        obj.matching_egress_rule_refs = []
        container = SerializationHelper.find_child_element(element, "MATCHING-EGRESS-RULE-REFS")
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
                    obj.matching_egress_rule_refs.append(child_value)

        # Parse matching_ingress_rule_refs (list from container "MATCHING-INGRESS-RULE-REFS")
        obj.matching_ingress_rule_refs = []
        container = SerializationHelper.find_child_element(element, "MATCHING-INGRESS-RULE-REFS")
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
                    obj.matching_ingress_rule_refs.append(child_value)

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
