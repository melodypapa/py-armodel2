"""FMFeatureSelectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature_models: list[FMFeatureModel]
    include_refs: list[ARRef]
    selections: list[FMFeatureSelection]
    def __init__(self) -> None:
        """Initialize FMFeatureSelectionSet."""
        super().__init__()
        self.feature_models: list[FMFeatureModel] = []
        self.include_refs: list[ARRef] = []
        self.selections: list[FMFeatureSelection] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureSelectionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureSelectionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature_models (list to container "FEATURE-MODELS")
        if self.feature_models:
            wrapper = ET.Element("FEATURE-MODELS")
            for item in self.feature_models:
                serialized = ARObject._serialize_item(item, "FMFeatureModel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize include_refs (list to container "INCLUDES")
        if self.include_refs:
            wrapper = ET.Element("INCLUDES")
            for item in self.include_refs:
                serialized = ARObject._serialize_item(item, "FMFeatureSelectionSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize selections (list to container "SELECTIONS")
        if self.selections:
            wrapper = ET.Element("SELECTIONS")
            for item in self.selections:
                serialized = ARObject._serialize_item(item, "FMFeatureSelection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelectionSet":
        """Deserialize XML element to FMFeatureSelectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureSelectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureSelectionSet, cls).deserialize(element)

        # Parse feature_models (list from container "FEATURE-MODELS")
        obj.feature_models = []
        container = ARObject._find_child_element(element, "FEATURE-MODELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.feature_models.append(child_value)

        # Parse include_refs (list from container "INCLUDES")
        obj.include_refs = []
        container = ARObject._find_child_element(element, "INCLUDES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.include_refs.append(child_value)

        # Parse selections (list from container "SELECTIONS")
        obj.selections = []
        container = ARObject._find_child_element(element, "SELECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.selections.append(child_value)

        return obj



class FMFeatureSelectionSetBuilder:
    """Builder for FMFeatureSelectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelectionSet = FMFeatureSelectionSet()

    def build(self) -> FMFeatureSelectionSet:
        """Build and return FMFeatureSelectionSet object.

        Returns:
            FMFeatureSelectionSet instance
        """
        # TODO: Add validation
        return self._obj
