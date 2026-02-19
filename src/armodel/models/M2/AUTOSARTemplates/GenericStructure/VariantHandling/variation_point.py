"""VariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1010)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2078)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 226)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class VariationPoint(ARObject):
    """AUTOSAR VariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint: Optional[DocumentationBlock]
    sw_syscond: Optional[ConditionByFormula]
    def __init__(self) -> None:
        """Initialize VariationPoint."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.sw_syscond: Optional[ConditionByFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize VariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize blueprint
        if self.blueprint is not None:
            serialized = ARObject._serialize_item(self.blueprint, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_syscond
        if self.sw_syscond is not None:
            serialized = ARObject._serialize_item(self.sw_syscond, "ConditionByFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-SYSCOND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPoint":
        """Deserialize XML element to VariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariationPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint
        child = ARObject._find_child_element(element, "BLUEPRINT")
        if child is not None:
            blueprint_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.blueprint = blueprint_value

        # Parse sw_syscond
        child = ARObject._find_child_element(element, "SW-SYSCOND")
        if child is not None:
            sw_syscond_value = ARObject._deserialize_by_tag(child, "ConditionByFormula")
            obj.sw_syscond = sw_syscond_value

        return obj



class VariationPointBuilder:
    """Builder for VariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPoint = VariationPoint()

    def build(self) -> VariationPoint:
        """Build and return VariationPoint object.

        Returns:
            VariationPoint instance
        """
        # TODO: Add validation
        return self._obj
