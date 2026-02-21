"""DataTransformationSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
    TransformationTechnology,
)


class DataTransformationSet(ARElement):
    """AUTOSAR DataTransformationSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    datas: list[DataTransformation]
    transformation_technologies: list[TransformationTechnology]
    def __init__(self) -> None:
        """Initialize DataTransformationSet."""
        super().__init__()
        self.datas: list[DataTransformation] = []
        self.transformation_technologies: list[TransformationTechnology] = []

    def serialize(self) -> ET.Element:
        """Serialize DataTransformationSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTransformationSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize datas (list to container "DATAS")
        if self.datas:
            wrapper = ET.Element("DATAS")
            for item in self.datas:
                serialized = SerializationHelper.serialize_item(item, "DataTransformation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformation_technologies (list to container "TRANSFORMATION-TECHNOLOGIES")
        if self.transformation_technologies:
            wrapper = ET.Element("TRANSFORMATION-TECHNOLOGIES")
            for item in self.transformation_technologies:
                serialized = SerializationHelper.serialize_item(item, "TransformationTechnology")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformationSet":
        """Deserialize XML element to DataTransformationSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformationSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTransformationSet, cls).deserialize(element)

        # Parse datas (list from container "DATAS")
        obj.datas = []
        container = SerializationHelper.find_child_element(element, "DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.datas.append(child_value)

        # Parse transformation_technologies (list from container "TRANSFORMATION-TECHNOLOGIES")
        obj.transformation_technologies = []
        container = SerializationHelper.find_child_element(element, "TRANSFORMATION-TECHNOLOGIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_technologies.append(child_value)

        return obj



class DataTransformationSetBuilder:
    """Builder for DataTransformationSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformationSet = DataTransformationSet()

    def build(self) -> DataTransformationSet:
        """Build and return DataTransformationSet object.

        Returns:
            DataTransformationSet instance
        """
        # TODO: Add validation
        return self._obj
