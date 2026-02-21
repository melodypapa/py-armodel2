"""EcucAddInfoParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class EcucAddInfoParamValue(EcucParameterValue):
    """AUTOSAR EcucAddInfoParamValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize EcucAddInfoParamValue."""
        super().__init__()
        self.value: Optional[DocumentationBlock] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAddInfoParamValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAddInfoParamValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "DocumentationBlock")
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
    def deserialize(cls, element: ET.Element) -> "EcucAddInfoParamValue":
        """Deserialize XML element to EcucAddInfoParamValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAddInfoParamValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAddInfoParamValue, cls).deserialize(element)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.value = value_value

        return obj



class EcucAddInfoParamValueBuilder:
    """Builder for EcucAddInfoParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAddInfoParamValue = EcucAddInfoParamValue()

    def build(self) -> EcucAddInfoParamValue:
        """Build and return EcucAddInfoParamValue object.

        Returns:
            EcucAddInfoParamValue instance
        """
        # TODO: Add validation
        return self._obj
