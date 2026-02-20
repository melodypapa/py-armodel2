"""EcucTextualParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 127)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class EcucTextualParamValue(EcucParameterValue):
    """AUTOSAR EcucTextualParamValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize EcucTextualParamValue."""
        super().__init__()
        self.value: Optional[VerbatimString] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucTextualParamValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucTextualParamValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucTextualParamValue":
        """Deserialize XML element to EcucTextualParamValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucTextualParamValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucTextualParamValue, cls).deserialize(element)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "VerbatimString")
            obj.value = value_value

        return obj



class EcucTextualParamValueBuilder:
    """Builder for EcucTextualParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucTextualParamValue = EcucTextualParamValue()

    def build(self) -> EcucTextualParamValue:
        """Build and return EcucTextualParamValue object.

        Returns:
            EcucTextualParamValue instance
        """
        # TODO: Add validation
        return self._obj
