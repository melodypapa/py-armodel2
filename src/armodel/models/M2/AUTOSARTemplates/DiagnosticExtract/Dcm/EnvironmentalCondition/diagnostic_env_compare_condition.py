"""DiagnosticEnvCompareCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import (
    DiagnosticCompareTypeEnum,
)
from abc import ABC, abstractmethod


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart, ABC):
    """AUTOSAR DiagnosticEnvCompareCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    compare_type: Optional[DiagnosticCompareTypeEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvCompareCondition."""
        super().__init__()
        self.compare_type: Optional[DiagnosticCompareTypeEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvCompareCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvCompareCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compare_type
        if self.compare_type is not None:
            serialized = ARObject._serialize_item(self.compare_type, "DiagnosticCompareTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPARE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvCompareCondition":
        """Deserialize XML element to DiagnosticEnvCompareCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvCompareCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvCompareCondition, cls).deserialize(element)

        # Parse compare_type
        child = ARObject._find_child_element(element, "COMPARE-TYPE")
        if child is not None:
            compare_type_value = DiagnosticCompareTypeEnum.deserialize(child)
            obj.compare_type = compare_type_value

        return obj



class DiagnosticEnvCompareConditionBuilder:
    """Builder for DiagnosticEnvCompareCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvCompareCondition = DiagnosticEnvCompareCondition()

    def build(self) -> DiagnosticEnvCompareCondition:
        """Build and return DiagnosticEnvCompareCondition object.

        Returns:
            DiagnosticEnvCompareCondition instance
        """
        # TODO: Add validation
        return self._obj
