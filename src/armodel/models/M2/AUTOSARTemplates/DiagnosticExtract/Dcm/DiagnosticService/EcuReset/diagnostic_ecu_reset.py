"""DiagnosticEcuReset AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticEcuReset."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_sub: Optional[PositiveInteger]
    ecu_reset_class: Optional[DiagnosticEcuReset]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuReset."""
        super().__init__()
        self.custom_sub: Optional[PositiveInteger] = None
        self.ecu_reset_class: Optional[DiagnosticEcuReset] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEcuReset to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEcuReset, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_sub
        if self.custom_sub is not None:
            serialized = ARObject._serialize_item(self.custom_sub, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_reset_class
        if self.ecu_reset_class is not None:
            serialized = ARObject._serialize_item(self.ecu_reset_class, "DiagnosticEcuReset")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-RESET-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuReset":
        """Deserialize XML element to DiagnosticEcuReset object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuReset object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuReset, cls).deserialize(element)

        # Parse custom_sub
        child = ARObject._find_child_element(element, "CUSTOM-SUB")
        if child is not None:
            custom_sub_value = child.text
            obj.custom_sub = custom_sub_value

        # Parse ecu_reset_class
        child = ARObject._find_child_element(element, "ECU-RESET-CLASS")
        if child is not None:
            ecu_reset_class_value = ARObject._deserialize_by_tag(child, "DiagnosticEcuReset")
            obj.ecu_reset_class = ecu_reset_class_value

        return obj



class DiagnosticEcuResetBuilder:
    """Builder for DiagnosticEcuReset."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuReset = DiagnosticEcuReset()

    def build(self) -> DiagnosticEcuReset:
        """Build and return DiagnosticEcuReset object.

        Returns:
            DiagnosticEcuReset instance
        """
        # TODO: Add validation
        return self._obj
