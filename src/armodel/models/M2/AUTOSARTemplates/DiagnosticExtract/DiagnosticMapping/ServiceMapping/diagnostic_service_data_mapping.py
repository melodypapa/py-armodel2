"""DiagnosticServiceDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 228)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_data_ref: Optional[ARRef]
    diagnostic_ref: Optional[ARRef]
    mapped_data_ref: Optional[ARRef]
    parameter: Optional[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceDataMapping."""
        super().__init__()
        self.diagnostic_data_ref: Optional[ARRef] = None
        self.diagnostic_ref: Optional[ARRef] = None
        self.mapped_data_ref: Optional[ARRef] = None
        self.parameter: Optional[DiagnosticParameter] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceDataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceDataMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_data_ref
        if self.diagnostic_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_data_ref, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_ref
        if self.diagnostic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_data_ref
        if self.mapped_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_data_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter
        if self.parameter is not None:
            serialized = SerializationHelper.serialize_item(self.parameter, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceDataMapping":
        """Deserialize XML element to DiagnosticServiceDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceDataMapping, cls).deserialize(element)

        # Parse diagnostic_data_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-DATA-REF")
        if child is not None:
            diagnostic_data_ref_value = ARRef.deserialize(child)
            obj.diagnostic_data_ref = diagnostic_data_ref_value

        # Parse diagnostic_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-REF")
        if child is not None:
            diagnostic_ref_value = ARRef.deserialize(child)
            obj.diagnostic_ref = diagnostic_ref_value

        # Parse mapped_data_ref
        child = SerializationHelper.find_child_element(element, "MAPPED-DATA-REF")
        if child is not None:
            mapped_data_ref_value = ARRef.deserialize(child)
            obj.mapped_data_ref = mapped_data_ref_value

        # Parse parameter
        child = SerializationHelper.find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticParameter")
            obj.parameter = parameter_value

        return obj



class DiagnosticServiceDataMappingBuilder:
    """Builder for DiagnosticServiceDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceDataMapping = DiagnosticServiceDataMapping()

    def build(self) -> DiagnosticServiceDataMapping:
        """Build and return DiagnosticServiceDataMapping object.

        Returns:
            DiagnosticServiceDataMapping instance
        """
        # TODO: Add validation
        return self._obj
