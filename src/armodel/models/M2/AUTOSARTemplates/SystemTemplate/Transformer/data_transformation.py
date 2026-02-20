"""DataTransformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 763)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DataTransformation(Identifiable):
    """AUTOSAR DataTransformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data: Optional[DataTransformationKindEnum]
    execute_despite: Optional[Boolean]
    transformers: list[Any]
    def __init__(self) -> None:
        """Initialize DataTransformation."""
        super().__init__()
        self.data: Optional[DataTransformationKindEnum] = None
        self.execute_despite: Optional[Boolean] = None
        self.transformers: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DataTransformation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTransformation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data
        if self.data is not None:
            serialized = ARObject._serialize_item(self.data, "DataTransformationKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execute_despite
        if self.execute_despite is not None:
            serialized = ARObject._serialize_item(self.execute_despite, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTE-DESPITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformers (list to container "TRANSFORMERS")
        if self.transformers:
            wrapper = ET.Element("TRANSFORMERS")
            for item in self.transformers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformation":
        """Deserialize XML element to DataTransformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTransformation, cls).deserialize(element)

        # Parse data
        child = ARObject._find_child_element(element, "DATA")
        if child is not None:
            data_value = DataTransformationKindEnum.deserialize(child)
            obj.data = data_value

        # Parse execute_despite
        child = ARObject._find_child_element(element, "EXECUTE-DESPITE")
        if child is not None:
            execute_despite_value = child.text
            obj.execute_despite = execute_despite_value

        # Parse transformers (list from container "TRANSFORMERS")
        obj.transformers = []
        container = ARObject._find_child_element(element, "TRANSFORMERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformers.append(child_value)

        return obj



class DataTransformationBuilder:
    """Builder for DataTransformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformation = DataTransformation()

    def build(self) -> DataTransformation:
        """Build and return DataTransformation object.

        Returns:
            DataTransformation instance
        """
        # TODO: Add validation
        return self._obj
