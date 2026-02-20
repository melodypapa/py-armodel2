"""PhysicalDimension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class PhysicalDimension(ARElement):
    """AUTOSAR PhysicalDimension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    current_exp: Optional[Numerical]
    length_exp: Optional[Numerical]
    luminous_intensity_exp: Optional[Numerical]
    mass_exp: Optional[Numerical]
    molar_amount_exp: Optional[Numerical]
    temperature_exp: Optional[Numerical]
    time_exp: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize PhysicalDimension."""
        super().__init__()
        self.current_exp: Optional[Numerical] = None
        self.length_exp: Optional[Numerical] = None
        self.luminous_intensity_exp: Optional[Numerical] = None
        self.mass_exp: Optional[Numerical] = None
        self.molar_amount_exp: Optional[Numerical] = None
        self.temperature_exp: Optional[Numerical] = None
        self.time_exp: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimension to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalDimension, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize current_exp
        if self.current_exp is not None:
            serialized = ARObject._serialize_item(self.current_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CURRENT-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length_exp
        if self.length_exp is not None:
            serialized = ARObject._serialize_item(self.length_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize luminous_intensity_exp
        if self.luminous_intensity_exp is not None:
            serialized = ARObject._serialize_item(self.luminous_intensity_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LUMINOUS-INTENSITY-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mass_exp
        if self.mass_exp is not None:
            serialized = ARObject._serialize_item(self.mass_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASS-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize molar_amount_exp
        if self.molar_amount_exp is not None:
            serialized = ARObject._serialize_item(self.molar_amount_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MOLAR-AMOUNT-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize temperature_exp
        if self.temperature_exp is not None:
            serialized = ARObject._serialize_item(self.temperature_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEMPERATURE-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_exp
        if self.time_exp is not None:
            serialized = ARObject._serialize_item(self.time_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimension":
        """Deserialize XML element to PhysicalDimension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimension object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimension, cls).deserialize(element)

        # Parse current_exp
        child = ARObject._find_child_element(element, "CURRENT-EXP")
        if child is not None:
            current_exp_value = child.text
            obj.current_exp = current_exp_value

        # Parse length_exp
        child = ARObject._find_child_element(element, "LENGTH-EXP")
        if child is not None:
            length_exp_value = child.text
            obj.length_exp = length_exp_value

        # Parse luminous_intensity_exp
        child = ARObject._find_child_element(element, "LUMINOUS-INTENSITY-EXP")
        if child is not None:
            luminous_intensity_exp_value = child.text
            obj.luminous_intensity_exp = luminous_intensity_exp_value

        # Parse mass_exp
        child = ARObject._find_child_element(element, "MASS-EXP")
        if child is not None:
            mass_exp_value = child.text
            obj.mass_exp = mass_exp_value

        # Parse molar_amount_exp
        child = ARObject._find_child_element(element, "MOLAR-AMOUNT-EXP")
        if child is not None:
            molar_amount_exp_value = child.text
            obj.molar_amount_exp = molar_amount_exp_value

        # Parse temperature_exp
        child = ARObject._find_child_element(element, "TEMPERATURE-EXP")
        if child is not None:
            temperature_exp_value = child.text
            obj.temperature_exp = temperature_exp_value

        # Parse time_exp
        child = ARObject._find_child_element(element, "TIME-EXP")
        if child is not None:
            time_exp_value = child.text
            obj.time_exp = time_exp_value

        return obj



class PhysicalDimensionBuilder:
    """Builder for PhysicalDimension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimension = PhysicalDimension()

    def build(self) -> PhysicalDimension:
        """Build and return PhysicalDimension object.

        Returns:
            PhysicalDimension instance
        """
        # TODO: Add validation
        return self._obj
