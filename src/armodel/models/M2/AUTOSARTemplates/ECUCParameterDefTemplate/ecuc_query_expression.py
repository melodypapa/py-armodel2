"""EcucQueryExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

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

    config_element_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcucQueryExpression."""
        super().__init__()
        self.config_element_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucQueryExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucQueryExpression, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize config_element_ref
        if self.config_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.config_element_ref, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-ELEMENT-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucQueryExpression, cls).deserialize(element)

        # Parse config_element_ref
        child = SerializationHelper.find_child_element(element, "CONFIG-ELEMENT-REF")
        if child is not None:
            config_element_ref_value = ARRef.deserialize(child)
            obj.config_element_ref = config_element_ref_value

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
