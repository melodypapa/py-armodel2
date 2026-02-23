"""TransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 772)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
    transformer_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototype_refs: list[ARRef] = []
        self.transformer_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformationISignalProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize cs_error_reaction
        if self.cs_error_reaction is not None:
            serialized = SerializationHelper.serialize_item(self.cs_error_reaction, "CSTransformerErrorReactionEnum")
            if serialized is not None:
                wrapped = ET.Element("CS-ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize data_prototype_refs (list from container "DATA-PROTOTYPE-REFS")
        if self.data_prototype_refs:
            container = ET.Element("DATA-PROTOTYPE-REFS")
            for item in self.data_prototype_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("DataPrototype", package_data):
                    # Simple primitive type
                    child = ET.Element("DATA-PROTOTYPE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("DataPrototype", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize transformer_ref
        if self.transformer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transformer_ref, "Any")
            if serialized is not None:
                wrapped = ET.Element("TRANSFORMER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationISignalProps":
        """Deserialize XML element to TransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationISignalProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformationISignalProps, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse cs_error_reaction
        child = SerializationHelper.find_child_element(inner_elem, "CS-ERROR-REACTION")
        if child is not None:
            cs_error_reaction_value = CSTransformerErrorReactionEnum.deserialize(child)
            obj.cs_error_reaction = cs_error_reaction_value

        # Parse data_prototype_refs (list from container "DATA-PROTOTYPE-REFS")
        obj.data_prototype_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "DATA-PROTOTYPE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("DataPrototype", package_data):
                    child_value = child.text
                elif is_enum_type("DataPrototype", package_data):
                    child_value = DataPrototype.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_prototype_refs.append(child_value)

        # Parse transformer_ref
        child = SerializationHelper.find_child_element(inner_elem, "TRANSFORMER-REF")
        if child is not None:
            transformer_ref_value = ARRef.deserialize(child)
            obj.transformer_ref = transformer_ref_value

        return obj



