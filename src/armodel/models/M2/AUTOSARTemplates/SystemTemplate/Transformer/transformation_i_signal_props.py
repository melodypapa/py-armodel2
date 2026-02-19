"""TransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 772)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from abc import ABC, abstractmethod


class TransformationISignalProps(ARObject, ABC):
    """AUTOSAR TransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cs_error_reaction: Optional[CSTransformerErrorReactionEnum]
    data_prototype_refs: list[ARRef]
    transformer: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototype_refs: list[ARRef] = []
        self.transformer: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize TransformationISignalProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize cs_error_reaction
        if self.cs_error_reaction is not None:
            serialized = ARObject._serialize_item(self.cs_error_reaction, "CSTransformerErrorReactionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CS-ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_prototype_refs (list to container "DATA-PROTOTYPES")
        if self.data_prototype_refs:
            wrapper = ET.Element("DATA-PROTOTYPES")
            for item in self.data_prototype_refs:
                serialized = ARObject._serialize_item(item, "DataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformer
        if self.transformer is not None:
            serialized = ARObject._serialize_item(self.transformer, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationISignalProps":
        """Deserialize XML element to TransformationISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationISignalProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cs_error_reaction
        child = ARObject._find_child_element(element, "CS-ERROR-REACTION")
        if child is not None:
            cs_error_reaction_value = CSTransformerErrorReactionEnum.deserialize(child)
            obj.cs_error_reaction = cs_error_reaction_value

        # Parse data_prototype_refs (list from container "DATA-PROTOTYPES")
        obj.data_prototype_refs = []
        container = ARObject._find_child_element(element, "DATA-PROTOTYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_prototype_refs.append(child_value)

        # Parse transformer
        child = ARObject._find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = child.text
            obj.transformer = transformer_value

        return obj



class TransformationISignalPropsBuilder:
    """Builder for TransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationISignalProps = TransformationISignalProps()

    def build(self) -> TransformationISignalProps:
        """Build and return TransformationISignalProps object.

        Returns:
            TransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
