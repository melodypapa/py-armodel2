"""SoConIPduIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SoConIPduIdentifier(Referrable):
    """AUTOSAR SoConIPduIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    header_id: Optional[PositiveInteger]
    pdu_collection_ref: Optional[Any]
    pdu_collection_trigger_ref: Optional[PduCollectionTriggerEnum]
    pdu_triggering_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SoConIPduIdentifier."""
        super().__init__()
        self.header_id: Optional[PositiveInteger] = None
        self.pdu_collection_ref: Optional[Any] = None
        self.pdu_collection_trigger_ref: Optional[PduCollectionTriggerEnum] = None
        self.pdu_triggering_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SoConIPduIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SoConIPduIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize header_id
        if self.header_id is not None:
            serialized = SerializationHelper.serialize_item(self.header_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_collection_ref
        if self.pdu_collection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_collection_trigger_ref
        if self.pdu_collection_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection_trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_triggering_ref
        if self.pdu_triggering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-TRIGGERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoConIPduIdentifier":
        """Deserialize XML element to SoConIPduIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoConIPduIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoConIPduIdentifier, cls).deserialize(element)

        # Parse header_id
        child = SerializationHelper.find_child_element(element, "HEADER-ID")
        if child is not None:
            header_id_value = child.text
            obj.header_id = header_id_value

        # Parse pdu_collection_ref
        child = SerializationHelper.find_child_element(element, "PDU-COLLECTION-REF")
        if child is not None:
            pdu_collection_ref_value = ARRef.deserialize(child)
            obj.pdu_collection_ref = pdu_collection_ref_value

        # Parse pdu_collection_trigger_ref
        child = SerializationHelper.find_child_element(element, "PDU-COLLECTION-TRIGGER-REF")
        if child is not None:
            pdu_collection_trigger_ref_value = ARRef.deserialize(child)
            obj.pdu_collection_trigger_ref = pdu_collection_trigger_ref_value

        # Parse pdu_triggering_ref
        child = SerializationHelper.find_child_element(element, "PDU-TRIGGERING-REF")
        if child is not None:
            pdu_triggering_ref_value = ARRef.deserialize(child)
            obj.pdu_triggering_ref = pdu_triggering_ref_value

        return obj



class SoConIPduIdentifierBuilder:
    """Builder for SoConIPduIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoConIPduIdentifier = SoConIPduIdentifier()

    def build(self) -> SoConIPduIdentifier:
        """Build and return SoConIPduIdentifier object.

        Returns:
            SoConIPduIdentifier instance
        """
        # TODO: Add validation
        return self._obj
