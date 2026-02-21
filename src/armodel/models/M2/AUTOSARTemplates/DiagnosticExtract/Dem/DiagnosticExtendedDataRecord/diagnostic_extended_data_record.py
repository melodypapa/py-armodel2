"""DiagnosticExtendedDataRecord AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticExtendedDataRecord.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame import (
    DiagnosticRecordTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticExtendedDataRecord(DiagnosticCommonElement):
    """AUTOSAR DiagnosticExtendedDataRecord."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_trigger: Optional[String]
    record_elements: list[DiagnosticParameter]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticExtendedDataRecord."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_elements: list[DiagnosticParameter] = []
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticExtendedDataRecord to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticExtendedDataRecord, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_trigger
        if self.custom_trigger is not None:
            serialized = SerializationHelper.serialize_item(self.custom_trigger, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize record_elements (list to container "RECORD-ELEMENTS")
        if self.record_elements:
            wrapper = ET.Element("RECORD-ELEMENTS")
            for item in self.record_elements:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize record_number
        if self.record_number is not None:
            serialized = SerializationHelper.serialize_item(self.record_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECORD-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger
        if self.trigger is not None:
            serialized = SerializationHelper.serialize_item(self.trigger, "DiagnosticRecordTriggerEnum")
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
            serialized = SerializationHelper.serialize_item(self.update, "Boolean")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticExtendedDataRecord":
        """Deserialize XML element to DiagnosticExtendedDataRecord object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticExtendedDataRecord object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticExtendedDataRecord, cls).deserialize(element)

        # Parse custom_trigger
        child = SerializationHelper.find_child_element(element, "CUSTOM-TRIGGER")
        if child is not None:
            custom_trigger_value = child.text
            obj.custom_trigger = custom_trigger_value

        # Parse record_elements (list from container "RECORD-ELEMENTS")
        obj.record_elements = []
        container = SerializationHelper.find_child_element(element, "RECORD-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.record_elements.append(child_value)

        # Parse record_number
        child = SerializationHelper.find_child_element(element, "RECORD-NUMBER")
        if child is not None:
            record_number_value = child.text
            obj.record_number = record_number_value

        # Parse trigger
        child = SerializationHelper.find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_value = DiagnosticRecordTriggerEnum.deserialize(child)
            obj.trigger = trigger_value

        # Parse update
        child = SerializationHelper.find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



class DiagnosticExtendedDataRecordBuilder:
    """Builder for DiagnosticExtendedDataRecord."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticExtendedDataRecord = DiagnosticExtendedDataRecord()

    def build(self) -> DiagnosticExtendedDataRecord:
        """Build and return DiagnosticExtendedDataRecord object.

        Returns:
            DiagnosticExtendedDataRecord instance
        """
        # TODO: Add validation
        return self._obj
