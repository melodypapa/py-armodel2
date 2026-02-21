"""EcucFloatParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 61)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    Limit,
)


class EcucFloatParamDef(EcucParameterDef):
    """AUTOSAR EcucFloatParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[Float]
    max: Optional[Limit]
    min: Optional[Limit]
    def __init__(self) -> None:
        """Initialize EcucFloatParamDef."""
        super().__init__()
        self.default_value: Optional[Float] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucFloatParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucFloatParamDef, self).serialize()

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
            serialized = ARObject._serialize_item(self.default_value, "Float")
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
            serialized = ARObject._serialize_item(self.max, "Limit")
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
            serialized = ARObject._serialize_item(self.min, "Limit")
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
    def deserialize(cls, element: ET.Element) -> "EcucFloatParamDef":
        """Deserialize XML element to EcucFloatParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucFloatParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucFloatParamDef, cls).deserialize(element)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.min = min_value

        return obj



class EcucFloatParamDefBuilder:
    """Builder for EcucFloatParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucFloatParamDef = EcucFloatParamDef()

    def build(self) -> EcucFloatParamDef:
        """Build and return EcucFloatParamDef object.

        Returns:
            EcucFloatParamDef instance
        """
        # TODO: Add validation
        return self._obj
