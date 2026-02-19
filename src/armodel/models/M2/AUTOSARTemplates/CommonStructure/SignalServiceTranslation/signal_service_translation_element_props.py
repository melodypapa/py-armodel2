"""SignalServiceTranslationElementProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 735)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    element_ref: Optional[ARRef]
    filter: Optional[DataFilter]
    transmission: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element_ref: Optional[ARRef] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationElementProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationElementProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_ref
        if self.element_ref is not None:
            serialized = ARObject._serialize_item(self.element_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter
        if self.filter is not None:
            serialized = ARObject._serialize_item(self.filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = ARObject._serialize_item(self.transmission, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationElementProps":
        """Deserialize XML element to SignalServiceTranslationElementProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationElementProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationElementProps, cls).deserialize(element)

        # Parse element_ref
        child = ARObject._find_child_element(element, "ELEMENT")
        if child is not None:
            element_ref_value = ARRef.deserialize(child)
            obj.element_ref = element_ref_value

        # Parse filter
        child = ARObject._find_child_element(element, "FILTER")
        if child is not None:
            filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.filter = filter_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class SignalServiceTranslationElementPropsBuilder:
    """Builder for SignalServiceTranslationElementProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()

    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return SignalServiceTranslationElementProps object.

        Returns:
            SignalServiceTranslationElementProps instance
        """
        # TODO: Add validation
        return self._obj
