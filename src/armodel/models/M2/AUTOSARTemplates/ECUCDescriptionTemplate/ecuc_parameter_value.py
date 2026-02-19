"""EcucParameterValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 124)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 189)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from abc import ABC, abstractmethod


class EcucParameterValue(EcucIndexableValue, ABC):
    """AUTOSAR EcucParameterValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotations: list[Annotation]
    definition: Optional[EcucParameterDef]
    is_auto_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucParameterValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition: Optional[EcucParameterDef] = None
        self.is_auto_value: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucParameterValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParameterValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize annotations (list to container "ANNOTATIONS")
        if self.annotations:
            wrapper = ET.Element("ANNOTATIONS")
            for item in self.annotations:
                serialized = ARObject._serialize_item(item, "Annotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize definition
        if self.definition is not None:
            serialized = ARObject._serialize_item(self.definition, "EcucParameterDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_auto_value
        if self.is_auto_value is not None:
            serialized = ARObject._serialize_item(self.is_auto_value, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-AUTO-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterValue":
        """Deserialize XML element to EcucParameterValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParameterValue, cls).deserialize(element)

        # Parse annotations (list from container "ANNOTATIONS")
        obj.annotations = []
        container = ARObject._find_child_element(element, "ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.annotations.append(child_value)

        # Parse definition
        child = ARObject._find_child_element(element, "DEFINITION")
        if child is not None:
            definition_value = ARObject._deserialize_by_tag(child, "EcucParameterDef")
            obj.definition = definition_value

        # Parse is_auto_value
        child = ARObject._find_child_element(element, "IS-AUTO-VALUE")
        if child is not None:
            is_auto_value_value = child.text
            obj.is_auto_value = is_auto_value_value

        return obj



class EcucParameterValueBuilder:
    """Builder for EcucParameterValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterValue = EcucParameterValue()

    def build(self) -> EcucParameterValue:
        """Build and return EcucParameterValue object.

        Returns:
            EcucParameterValue instance
        """
        # TODO: Add validation
        return self._obj
