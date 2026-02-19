"""ContainedIPduProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainedIPduProps(ARObject):
    """AUTOSAR ContainedIPduProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    collection: Optional[Any]
    contained_pdu_ref: Optional[ARRef]
    header_id_long: Optional[PositiveInteger]
    header_id_short: Optional[PositiveInteger]
    offset: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    timeout: Optional[TimeValue]
    trigger_ref: Optional[ARRef]
    update: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()
        self.collection: Optional[Any] = None
        self.contained_pdu_ref: Optional[ARRef] = None
        self.header_id_long: Optional[PositiveInteger] = None
        self.header_id_short: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.timeout: Optional[TimeValue] = None
        self.trigger_ref: Optional[ARRef] = None
        self.update: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize ContainedIPduProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize collection
        if self.collection is not None:
            serialized = ARObject._serialize_item(self.collection, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contained_pdu_ref
        if self.contained_pdu_ref is not None:
            serialized = ARObject._serialize_item(self.contained_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINED-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_id_long
        if self.header_id_long is not None:
            serialized = ARObject._serialize_item(self.header_id_long, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_id_short
        if self.header_id_short is not None:
            serialized = ARObject._serialize_item(self.header_id_short, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = ARObject._serialize_item(self.offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = ARObject._serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = ARObject._serialize_item(self.trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update
        if self.update is not None:
            serialized = ARObject._serialize_item(self.update, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainedIPduProps":
        """Deserialize XML element to ContainedIPduProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ContainedIPduProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse collection
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_value = child.text
            obj.collection = collection_value

        # Parse contained_pdu_ref
        child = ARObject._find_child_element(element, "CONTAINED-PDU")
        if child is not None:
            contained_pdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.contained_pdu_ref = contained_pdu_ref_value

        # Parse header_id_long
        child = ARObject._find_child_element(element, "HEADER-ID-LONG")
        if child is not None:
            header_id_long_value = child.text
            obj.header_id_long = header_id_long_value

        # Parse header_id_short
        child = ARObject._find_child_element(element, "HEADER-ID-SHORT")
        if child is not None:
            header_id_short_value = child.text
            obj.header_id_short = header_id_short_value

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = PduCollectionTriggerEnum.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        # Parse update
        child = ARObject._find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



class ContainedIPduPropsBuilder:
    """Builder for ContainedIPduProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainedIPduProps = ContainedIPduProps()

    def build(self) -> ContainedIPduProps:
        """Build and return ContainedIPduProps object.

        Returns:
            ContainedIPduProps instance
        """
        # TODO: Add validation
        return self._obj
