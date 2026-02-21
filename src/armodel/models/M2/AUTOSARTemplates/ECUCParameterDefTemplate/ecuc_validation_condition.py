"""EcucValidationCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
        EcucConditionFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
        EcucQuery,
    )



class EcucValidationCondition(Identifiable):
    """AUTOSAR EcucValidationCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_queries: list[EcucQuery]
    validation: Optional[EcucConditionFormula]
    def __init__(self) -> None:
        """Initialize EcucValidationCondition."""
        super().__init__()
        self.ecuc_queries: list[EcucQuery] = []
        self.validation: Optional[EcucConditionFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucValidationCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucValidationCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_queries (list to container "ECUC-QUERIES")
        if self.ecuc_queries:
            wrapper = ET.Element("ECUC-QUERIES")
            for item in self.ecuc_queries:
                serialized = SerializationHelper.serialize_item(item, "EcucQuery")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize validation
        if self.validation is not None:
            serialized = SerializationHelper.serialize_item(self.validation, "EcucConditionFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValidationCondition":
        """Deserialize XML element to EcucValidationCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValidationCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucValidationCondition, cls).deserialize(element)

        # Parse ecuc_queries (list from container "ECUC-QUERIES")
        obj.ecuc_queries = []
        container = SerializationHelper.find_child_element(element, "ECUC-QUERIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecuc_queries.append(child_value)

        # Parse validation
        child = SerializationHelper.find_child_element(element, "VALIDATION")
        if child is not None:
            validation_value = SerializationHelper.deserialize_by_tag(child, "EcucConditionFormula")
            obj.validation = validation_value

        return obj



class EcucValidationConditionBuilder:
    """Builder for EcucValidationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValidationCondition = EcucValidationCondition()

    def build(self) -> EcucValidationCondition:
        """Build and return EcucValidationCondition object.

        Returns:
            EcucValidationCondition instance
        """
        # TODO: Add validation
        return self._obj
