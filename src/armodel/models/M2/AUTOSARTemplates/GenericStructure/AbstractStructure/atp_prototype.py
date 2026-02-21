"""AtpPrototype AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
    AtpType,
)
from abc import ABC, abstractmethod


class AtpPrototype(Identifiable, ABC):
    """AUTOSAR AtpPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_type_ref: ARRef
    def __init__(self) -> None:
        """Initialize AtpPrototype."""
        super().__init__()
        self.atp_type_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AtpPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_type_ref
        if self.atp_type_ref is not None:
            serialized = ARObject._serialize_item(self.atp_type_ref, "AtpType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpPrototype":
        """Deserialize XML element to AtpPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpPrototype, cls).deserialize(element)

        # Parse atp_type_ref
        child = ARObject._find_child_element(element, "ATP-TYPE-REF")
        if child is not None:
            atp_type_ref_value = ARRef.deserialize(child)
            obj.atp_type_ref = atp_type_ref_value

        return obj



class AtpPrototypeBuilder:
    """Builder for AtpPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpPrototype = AtpPrototype()

    def build(self) -> AtpPrototype:
        """Build and return AtpPrototype object.

        Returns:
            AtpPrototype instance
        """
        # TODO: Add validation
        return self._obj
