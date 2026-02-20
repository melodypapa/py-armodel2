"""Unit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 333)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)


class Unit(ARElement):
    """AUTOSAR Unit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    display_name: Optional[SingleLanguageUnitNames]
    factor_si_to_unit: Optional[Float]
    offset_si_to_unit: Optional[Float]
    physical_dimension_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize Unit."""
        super().__init__()
        self.display_name: Optional[SingleLanguageUnitNames] = None
        self.factor_si_to_unit: Optional[Float] = None
        self.offset_si_to_unit: Optional[Float] = None
        self.physical_dimension_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize Unit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Unit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize display_name
        if self.display_name is not None:
            serialized = ARObject._serialize_item(self.display_name, "SingleLanguageUnitNames")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISPLAY-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize factor_si_to_unit
        if self.factor_si_to_unit is not None:
            serialized = ARObject._serialize_item(self.factor_si_to_unit, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FACTOR-SI-TO-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset_si_to_unit
        if self.offset_si_to_unit is not None:
            serialized = ARObject._serialize_item(self.offset_si_to_unit, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-SI-TO-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_dimension_ref
        if self.physical_dimension_ref is not None:
            serialized = ARObject._serialize_item(self.physical_dimension_ref, "physicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-DIMENSION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Unit":
        """Deserialize XML element to Unit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Unit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Unit, cls).deserialize(element)

        # Parse display_name
        child = ARObject._find_child_element(element, "DISPLAY-NAME")
        if child is not None:
            display_name_value = ARObject._deserialize_by_tag(child, "SingleLanguageUnitNames")
            obj.display_name = display_name_value

        # Parse factor_si_to_unit
        child = ARObject._find_child_element(element, "FACTOR-SI-TO-UNIT")
        if child is not None:
            factor_si_to_unit_value = child.text
            obj.factor_si_to_unit = factor_si_to_unit_value

        # Parse offset_si_to_unit
        child = ARObject._find_child_element(element, "OFFSET-SI-TO-UNIT")
        if child is not None:
            offset_si_to_unit_value = child.text
            obj.offset_si_to_unit = offset_si_to_unit_value

        # Parse physical_dimension_ref
        child = ARObject._find_child_element(element, "PHYSICAL-DIMENSION-REF")
        if child is not None:
            physical_dimension_ref_value = ARRef.deserialize(child)
            obj.physical_dimension_ref = physical_dimension_ref_value

        return obj



class UnitBuilder:
    """Builder for Unit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Unit = Unit()

    def build(self) -> Unit:
        """Build and return Unit object.

        Returns:
            Unit instance
        """
        # TODO: Add validation
        return self._obj
