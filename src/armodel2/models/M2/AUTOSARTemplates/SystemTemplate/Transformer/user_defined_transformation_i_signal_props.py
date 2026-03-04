"""UserDefinedTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 828)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_variant()

class UserDefinedTransformationISignalProps(ARObject):
    """AUTOSAR UserDefinedTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS"


    def __init__(self) -> None:
        """Initialize UserDefinedTransformationISignalProps."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize UserDefinedTransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedTransformationISignalProps, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "UserDefinedTransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationISignalProps":
        """Deserialize XML element to UserDefinedTransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedTransformationISignalProps object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "UserDefinedTransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(UserDefinedTransformationISignalProps, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        return obj



class UserDefinedTransformationISignalPropsBuilder(BuilderBase):
    """Builder for UserDefinedTransformationISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UserDefinedTransformationISignalProps = UserDefinedTransformationISignalProps()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UserDefinedTransformationISignalProps:
        """Build and return the UserDefinedTransformationISignalProps instance with validation."""
        self._validate_instance()
        return self._obj