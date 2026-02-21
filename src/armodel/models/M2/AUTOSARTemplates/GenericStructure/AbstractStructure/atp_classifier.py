"""AtpClassifier AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from abc import ABC, abstractmethod


class AtpClassifier(Identifiable, ABC):
    """AUTOSAR AtpClassifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_features: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize AtpClassifier."""
        super().__init__()
        self.atp_features: list[AtpFeature] = []

    def serialize(self) -> ET.Element:
        """Serialize AtpClassifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpClassifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_features (list to container "ATP-FEATURES")
        if self.atp_features:
            wrapper = ET.Element("ATP-FEATURES")
            for item in self.atp_features:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpClassifier":
        """Deserialize XML element to AtpClassifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpClassifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpClassifier, cls).deserialize(element)

        # Parse atp_features (list from container "ATP-FEATURES")
        obj.atp_features = []
        container = SerializationHelper.find_child_element(element, "ATP-FEATURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.atp_features.append(child_value)

        return obj



class AtpClassifierBuilder:
    """Builder for AtpClassifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpClassifier = AtpClassifier()

    def build(self) -> AtpClassifier:
        """Build and return AtpClassifier object.

        Returns:
            AtpClassifier instance
        """
        # TODO: Add validation
        return self._obj
