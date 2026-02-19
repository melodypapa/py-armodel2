"""EcucBooleanParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 58)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucBooleanParamDef(EcucParameterDef):
    """AUTOSAR EcucBooleanParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucBooleanParamDef."""
        super().__init__()
        self.default_value: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucBooleanParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucBooleanParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = ARObject._serialize_item(self.default_value, "Boolean")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucBooleanParamDef":
        """Deserialize XML element to EcucBooleanParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucBooleanParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucBooleanParamDef, cls).deserialize(element)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        return obj



class EcucBooleanParamDefBuilder:
    """Builder for EcucBooleanParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucBooleanParamDef = EcucBooleanParamDef()

    def build(self) -> EcucBooleanParamDef:
        """Build and return EcucBooleanParamDef object.

        Returns:
            EcucBooleanParamDef instance
        """
        # TODO: Add validation
        return self._obj
