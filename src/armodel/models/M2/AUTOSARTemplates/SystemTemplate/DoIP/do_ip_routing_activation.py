"""DoIpRoutingActivation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 553)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_target_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_target_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DoIpRoutingActivation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpRoutingActivation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_target_refs (list to container "DO-IP-TARGET-REFS")
        if self.do_ip_target_refs:
            wrapper = ET.Element("DO-IP-TARGET-REFS")
            for item in self.do_ip_target_refs:
                serialized = SerializationHelper.serialize_item(item, "DoIpLogicTargetAddressProps")
                if serialized is not None:
                    child_elem = ET.Element("DO-IP-TARGET-REF")
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
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivation":
        """Deserialize XML element to DoIpRoutingActivation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpRoutingActivation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpRoutingActivation, cls).deserialize(element)

        # Parse do_ip_target_refs (list from container "DO-IP-TARGET-REFS")
        obj.do_ip_target_refs = []
        container = SerializationHelper.find_child_element(element, "DO-IP-TARGET-REFS")
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
                    obj.do_ip_target_refs.append(child_value)

        return obj



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
