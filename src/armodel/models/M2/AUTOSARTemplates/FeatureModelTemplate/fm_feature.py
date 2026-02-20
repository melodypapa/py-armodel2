"""FMFeature AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 24)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
    FMFeatureRestriction,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
        FMFeatureRelation,
    )



class FMFeature(ARElement):
    """AUTOSAR FMFeature."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_defs: list[FMAttributeDef]
    decomposition_decompositions: list[FMFeature]
    maximum: Optional[BindingTimeEnum]
    minimum: Optional[BindingTimeEnum]
    relations: list[FMFeatureRelation]
    restrictions: list[FMFeatureRestriction]
    def __init__(self) -> None:
        """Initialize FMFeature."""
        super().__init__()
        self.attribute_defs: list[FMAttributeDef] = []
        self.decomposition_decompositions: list[FMFeature] = []
        self.maximum: Optional[BindingTimeEnum] = None
        self.minimum: Optional[BindingTimeEnum] = None
        self.relations: list[FMFeatureRelation] = []
        self.restrictions: list[FMFeatureRestriction] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeature to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeature, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_defs (list to container "ATTRIBUTE-DEFS")
        if self.attribute_defs:
            wrapper = ET.Element("ATTRIBUTE-DEFS")
            for item in self.attribute_defs:
                serialized = ARObject._serialize_item(item, "FMAttributeDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize decomposition_decompositions (list to container "DECOMPOSITION-DECOMPOSITIONS")
        if self.decomposition_decompositions:
            wrapper = ET.Element("DECOMPOSITION-DECOMPOSITIONS")
            for item in self.decomposition_decompositions:
                serialized = ARObject._serialize_item(item, "FMFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize maximum
        if self.maximum is not None:
            serialized = ARObject._serialize_item(self.maximum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = ARObject._serialize_item(self.minimum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize relations (list to container "RELATIONS")
        if self.relations:
            wrapper = ET.Element("RELATIONS")
            for item in self.relations:
                serialized = ARObject._serialize_item(item, "FMFeatureRelation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize restrictions (list to container "RESTRICTIONS")
        if self.restrictions:
            wrapper = ET.Element("RESTRICTIONS")
            for item in self.restrictions:
                serialized = ARObject._serialize_item(item, "FMFeatureRestriction")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeature":
        """Deserialize XML element to FMFeature object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeature object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeature, cls).deserialize(element)

        # Parse attribute_defs (list from container "ATTRIBUTE-DEFS")
        obj.attribute_defs = []
        container = ARObject._find_child_element(element, "ATTRIBUTE-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attribute_defs.append(child_value)

        # Parse decomposition_decompositions (list from container "DECOMPOSITION-DECOMPOSITIONS")
        obj.decomposition_decompositions = []
        container = ARObject._find_child_element(element, "DECOMPOSITION-DECOMPOSITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.decomposition_decompositions.append(child_value)

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = BindingTimeEnum.deserialize(child)
            obj.maximum = maximum_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = BindingTimeEnum.deserialize(child)
            obj.minimum = minimum_value

        # Parse relations (list from container "RELATIONS")
        obj.relations = []
        container = ARObject._find_child_element(element, "RELATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.relations.append(child_value)

        # Parse restrictions (list from container "RESTRICTIONS")
        obj.restrictions = []
        container = ARObject._find_child_element(element, "RESTRICTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.restrictions.append(child_value)

        return obj



class FMFeatureBuilder:
    """Builder for FMFeature."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeature = FMFeature()

    def build(self) -> FMFeature:
        """Build and return FMFeature object.

        Returns:
            FMFeature instance
        """
        # TODO: Add validation
        return self._obj
