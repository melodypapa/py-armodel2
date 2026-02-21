"""AbstractVariationRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 104)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class AbstractVariationRestriction(ARObject, ABC):
    """AUTOSAR AbstractVariationRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    valid_bindings: list[FullBindingTimeEnum]
    variation: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize AbstractVariationRestriction."""
        super().__init__()
        self.valid_bindings: list[FullBindingTimeEnum] = []
        self.variation: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractVariationRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractVariationRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize valid_bindings (list to container "VALID-BINDINGS")
        if self.valid_bindings:
            wrapper = ET.Element("VALID-BINDINGS")
            for item in self.valid_bindings:
                serialized = SerializationHelper.serialize_item(item, "FullBindingTimeEnum")
                if serialized is not None:
                    child_elem = ET.Element("VALID-BINDING")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variation
        if self.variation is not None:
            serialized = SerializationHelper.serialize_item(self.variation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractVariationRestriction":
        """Deserialize XML element to AbstractVariationRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractVariationRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractVariationRestriction, cls).deserialize(element)

        # Parse valid_bindings (list from container "VALID-BINDINGS")
        obj.valid_bindings = []
        container = SerializationHelper.find_child_element(element, "VALID-BINDINGS")
        if container is not None:
            for child in container:
                # Extract enum value (FullBindingTimeEnum)
                child_value = FullBindingTimeEnum.deserialize(child)
                if child_value is not None:
                    obj.valid_bindings.append(child_value)

        # Parse variation
        child = SerializationHelper.find_child_element(element, "VARIATION")
        if child is not None:
            variation_value = child.text
            obj.variation = variation_value

        return obj



class AbstractVariationRestrictionBuilder:
    """Builder for AbstractVariationRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractVariationRestriction = AbstractVariationRestriction()

    def build(self) -> AbstractVariationRestriction:
        """Build and return AbstractVariationRestriction object.

        Returns:
            AbstractVariationRestriction instance
        """
        # TODO: Add validation
        return self._obj
