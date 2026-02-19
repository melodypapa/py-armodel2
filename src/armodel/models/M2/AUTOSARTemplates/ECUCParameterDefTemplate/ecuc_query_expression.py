"""EcucQueryExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
        EcucDefinitionElement,
    )



class EcucQueryExpression(ARObject):
    """AUTOSAR EcucQueryExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    config_element: Optional[EcucDefinitionElement]
    def __init__(self) -> None:
        """Initialize EcucQueryExpression."""
        super().__init__()
        self.config_element: Optional[EcucDefinitionElement] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucQueryExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize config_element
        if self.config_element is not None:
            serialized = ARObject._serialize_item(self.config_element, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucQueryExpression":
        """Deserialize XML element to EcucQueryExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucQueryExpression object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse config_element
        child = ARObject._find_child_element(element, "CONFIG-ELEMENT")
        if child is not None:
            config_element_value = ARObject._deserialize_by_tag(child, "EcucDefinitionElement")
            obj.config_element = config_element_value

        return obj



class EcucQueryExpressionBuilder:
    """Builder for EcucQueryExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucQueryExpression = EcucQueryExpression()

    def build(self) -> EcucQueryExpression:
        """Build and return EcucQueryExpression object.

        Returns:
            EcucQueryExpression instance
        """
        # TODO: Add validation
        return self._obj
