"""SignalServiceTranslationEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 731)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SignalServiceTranslationEventProps(Identifiable):
    """AUTOSAR SignalServiceTranslationEventProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    element_propses: list[Any]
    safe_translation: Optional[Boolean]
    secure: Optional[Boolean]
    translation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationEventProps."""
        super().__init__()
        self.element_propses: list[Any] = []
        self.safe_translation: Optional[Boolean] = None
        self.secure: Optional[Boolean] = None
        self.translation_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationEventProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationEventProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_propses (list to container "ELEMENT-PROPSES")
        if self.element_propses:
            wrapper = ET.Element("ELEMENT-PROPSES")
            for item in self.element_propses:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize safe_translation
        if self.safe_translation is not None:
            serialized = ARObject._serialize_item(self.safe_translation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAFE-TRANSLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secure
        if self.secure is not None:
            serialized = ARObject._serialize_item(self.secure, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize translation_ref
        if self.translation_ref is not None:
            serialized = ARObject._serialize_item(self.translation_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationEventProps":
        """Deserialize XML element to SignalServiceTranslationEventProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationEventProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationEventProps, cls).deserialize(element)

        # Parse element_propses (list from container "ELEMENT-PROPSES")
        obj.element_propses = []
        container = ARObject._find_child_element(element, "ELEMENT-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_propses.append(child_value)

        # Parse safe_translation
        child = ARObject._find_child_element(element, "SAFE-TRANSLATION")
        if child is not None:
            safe_translation_value = child.text
            obj.safe_translation = safe_translation_value

        # Parse secure
        child = ARObject._find_child_element(element, "SECURE")
        if child is not None:
            secure_value = child.text
            obj.secure = secure_value

        # Parse translation_ref
        child = ARObject._find_child_element(element, "TRANSLATION")
        if child is not None:
            translation_ref_value = ARRef.deserialize(child)
            obj.translation_ref = translation_ref_value

        return obj



class SignalServiceTranslationEventPropsBuilder:
    """Builder for SignalServiceTranslationEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationEventProps = SignalServiceTranslationEventProps()

    def build(self) -> SignalServiceTranslationEventProps:
        """Build and return SignalServiceTranslationEventProps object.

        Returns:
            SignalServiceTranslationEventProps instance
        """
        # TODO: Add validation
        return self._obj
