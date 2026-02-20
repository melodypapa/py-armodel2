"""DiagnosticReadDataByPeriodicID AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDataByPeriodicID."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_data_class_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicID."""
        super().__init__()
        self.read_data_class_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadDataByPeriodicID to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadDataByPeriodicID, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize read_data_class_ref
        if self.read_data_class_ref is not None:
            serialized = ARObject._serialize_item(self.read_data_class_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-DATA-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicID":
        """Deserialize XML element to DiagnosticReadDataByPeriodicID object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByPeriodicID object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByPeriodicID, cls).deserialize(element)

        # Parse read_data_class_ref
        child = ARObject._find_child_element(element, "READ-DATA-CLASS-REF")
        if child is not None:
            read_data_class_ref_value = ARRef.deserialize(child)
            obj.read_data_class_ref = read_data_class_ref_value

        return obj



class DiagnosticReadDataByPeriodicIDBuilder:
    """Builder for DiagnosticReadDataByPeriodicID."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicID = DiagnosticReadDataByPeriodicID()

    def build(self) -> DiagnosticReadDataByPeriodicID:
        """Build and return DiagnosticReadDataByPeriodicID object.

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # TODO: Add validation
        return self._obj
