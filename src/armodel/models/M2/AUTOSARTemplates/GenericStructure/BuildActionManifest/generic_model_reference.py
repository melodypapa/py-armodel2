"""GenericModelReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Ref,
)


class GenericModelReference(ARObject):
    """AUTOSAR GenericModelReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: NameToken
    dest: NameToken
    ref_ref: Ref
    def __init__(self) -> None:
        """Initialize GenericModelReference."""
        super().__init__()
        self.base: NameToken = None
        self.dest: NameToken = None
        self.ref_ref: Ref = None
    def serialize(self) -> ET.Element:
        """Serialize GenericModelReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dest
        if self.dest is not None:
            serialized = ARObject._serialize_item(self.dest, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ref_ref
        if self.ref_ref is not None:
            serialized = ARObject._serialize_item(self.ref_ref, "Ref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericModelReference":
        """Deserialize XML element to GenericModelReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GenericModelReference object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = child.text
            obj.base = base_value

        # Parse dest
        child = ARObject._find_child_element(element, "DEST")
        if child is not None:
            dest_value = child.text
            obj.dest = dest_value

        # Parse ref_ref
        child = ARObject._find_child_element(element, "REF")
        if child is not None:
            ref_ref_value = ARRef.deserialize(child)
            obj.ref_ref = ref_ref_value

        return obj



class GenericModelReferenceBuilder:
    """Builder for GenericModelReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericModelReference = GenericModelReference()

    def build(self) -> GenericModelReference:
        """Build and return GenericModelReference object.

        Returns:
            GenericModelReference instance
        """
        # TODO: Add validation
        return self._obj
