"""ConditionByFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 231)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)


class ConditionByFormula(ARObject):
    """AUTOSAR ConditionByFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    binding_time_enum: BindingTimeEnum
    def __init__(self) -> None:
        """Initialize ConditionByFormula."""
        super().__init__()
        self.binding_time_enum: BindingTimeEnum = None

    def serialize(self) -> ET.Element:
        """Serialize ConditionByFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize binding_time_enum
        if self.binding_time_enum is not None:
            serialized = ARObject._serialize_item(self.binding_time_enum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BINDING-TIME-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionByFormula":
        """Deserialize XML element to ConditionByFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConditionByFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse binding_time_enum
        child = ARObject._find_child_element(element, "BINDING-TIME-ENUM")
        if child is not None:
            binding_time_enum_value = BindingTimeEnum.deserialize(child)
            obj.binding_time_enum = binding_time_enum_value

        return obj



class ConditionByFormulaBuilder:
    """Builder for ConditionByFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionByFormula = ConditionByFormula()

    def build(self) -> ConditionByFormula:
        """Build and return ConditionByFormula object.

        Returns:
            ConditionByFormula instance
        """
        # TODO: Add validation
        return self._obj
