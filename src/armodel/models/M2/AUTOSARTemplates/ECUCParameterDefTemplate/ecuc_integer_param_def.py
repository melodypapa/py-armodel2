"""EcucIntegerParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)


class EcucIntegerParamDef(EcucParameterDef):
    """AUTOSAR EcucIntegerParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[UnlimitedInteger]
    max: Optional[UnlimitedInteger]
    min: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize EcucIntegerParamDef."""
        super().__init__()
        self.default_value: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucIntegerParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucIntegerParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIntegerParamDef":
        """Deserialize XML element to EcucIntegerParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucIntegerParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucIntegerParamDef, cls).deserialize(element)

        # Parse default_value
        child = SerializationHelper.find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse max
        child = SerializationHelper.find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = SerializationHelper.find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class EcucIntegerParamDefBuilder:
    """Builder for EcucIntegerParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIntegerParamDef = EcucIntegerParamDef()

    def build(self) -> EcucIntegerParamDef:
        """Build and return EcucIntegerParamDef object.

        Returns:
            EcucIntegerParamDef instance
        """
        # TODO: Add validation
        return self._obj
