"""DiagnosticEnvModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_element_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeCondition."""
        super().__init__()
        self.mode_element_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvModeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvModeCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_element_ref
        if self.mode_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_element_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvModeCondition":
        """Deserialize XML element to DiagnosticEnvModeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvModeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvModeCondition, cls).deserialize(element)

        # Parse mode_element_ref
        child = SerializationHelper.find_child_element(element, "MODE-ELEMENT-REF")
        if child is not None:
            mode_element_ref_value = ARRef.deserialize(child)
            obj.mode_element_ref = mode_element_ref_value

        return obj



class DiagnosticEnvModeConditionBuilder:
    """Builder for DiagnosticEnvModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvModeCondition = DiagnosticEnvModeCondition()

    def build(self) -> DiagnosticEnvModeCondition:
        """Build and return DiagnosticEnvModeCondition object.

        Returns:
            DiagnosticEnvModeCondition instance
        """
        # TODO: Add validation
        return self._obj
