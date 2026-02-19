"""EcucNumericalParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 128)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class EcucNumericalParamValue(EcucParameterValue):
    """AUTOSAR EcucNumericalParamValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize EcucNumericalParamValue."""
        super().__init__()
        self.value: Optional[Numerical] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucNumericalParamValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucNumericalParamValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "Numerical")
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
    def deserialize(cls, element: ET.Element) -> "EcucNumericalParamValue":
        """Deserialize XML element to EcucNumericalParamValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucNumericalParamValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucNumericalParamValue, cls).deserialize(element)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class EcucNumericalParamValueBuilder:
    """Builder for EcucNumericalParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucNumericalParamValue = EcucNumericalParamValue()

    def build(self) -> EcucNumericalParamValue:
        """Build and return EcucNumericalParamValue object.

        Returns:
            EcucNumericalParamValue instance
        """
        # TODO: Add validation
        return self._obj
