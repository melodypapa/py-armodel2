"""PduActivationRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 488)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_group_ref: Optional[EventGroupControlTypeEnum]
    i_pdu_identifier_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[EventGroupControlTypeEnum] = None
        self.i_pdu_identifier_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PduActivationRoutingGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduActivationRoutingGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_group_ref
        if self.event_group_ref is not None:
            serialized = ARObject._serialize_item(self.event_group_ref, "EventGroupControlTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_identifier_refs (list to container "I-PDU-IDENTIFIER-REFS")
        if self.i_pdu_identifier_refs:
            wrapper = ET.Element("I-PDU-IDENTIFIER-REFS")
            for item in self.i_pdu_identifier_refs:
                serialized = ARObject._serialize_item(item, "SoConIPduIdentifier")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-IDENTIFIER-REF")
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
    def deserialize(cls, element: ET.Element) -> "PduActivationRoutingGroup":
        """Deserialize XML element to PduActivationRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduActivationRoutingGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduActivationRoutingGroup, cls).deserialize(element)

        # Parse event_group_ref
        child = ARObject._find_child_element(element, "EVENT-GROUP-REF")
        if child is not None:
            event_group_ref_value = ARRef.deserialize(child)
            obj.event_group_ref = event_group_ref_value

        # Parse i_pdu_identifier_refs (list from container "I-PDU-IDENTIFIER-REFS")
        obj.i_pdu_identifier_refs = []
        container = ARObject._find_child_element(element, "I-PDU-IDENTIFIER-REFS")
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
                    obj.i_pdu_identifier_refs.append(child_value)

        return obj



class PduActivationRoutingGroupBuilder:
    """Builder for PduActivationRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()

    def build(self) -> PduActivationRoutingGroup:
        """Build and return PduActivationRoutingGroup object.

        Returns:
            PduActivationRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
