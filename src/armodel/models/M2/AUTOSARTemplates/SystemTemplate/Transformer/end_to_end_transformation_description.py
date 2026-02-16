"""EndToEndTransformationDescription AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationDescription(TransformationDescription):
    """AUTOSAR EndToEndTransformationDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("clear_from_valid", None, True, False, None),  # clearFromValid
        ("counter_offset", None, True, False, None),  # counterOffset
        ("crc_offset", None, True, False, None),  # crcOffset
        ("data_id_mode", None, False, False, DataIdModeEnum),  # dataIdMode
        ("data_id_nibble", None, True, False, None),  # dataIdNibble
        ("e2e_profile", None, False, False, E2EProfileCompatibilityProps),  # e2eProfile
        ("max_delta", None, True, False, None),  # maxDelta
        ("max_error_state", None, True, False, None),  # maxErrorState
        ("max_no_new_or", None, True, False, None),  # maxNoNewOr
        ("min_ok_state_init", None, True, False, None),  # minOkStateInit
        ("min_ok_state", None, True, False, None),  # minOkState
        ("offset", None, True, False, None),  # offset
        ("profile_behavior_behavior_enum", None, False, False, EndToEndProfileBehaviorEnum),  # profileBehaviorBehaviorEnum
        ("profile_name", None, True, False, None),  # profileName
        ("sync_counter_init", None, True, False, None),  # syncCounterInit
        ("upper_header", None, True, False, None),  # upperHeader
        ("window_size_init", None, True, False, None),  # windowSizeInit
        ("window_size", None, True, False, None),  # windowSize
    ]

    def __init__(self) -> None:
        """Initialize EndToEndTransformationDescription."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[DataIdModeEnum] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.profile_behavior_behavior_enum: Optional[EndToEndProfileBehaviorEnum] = None
        self.profile_name: Optional[NameToken] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.upper_header: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndTransformationDescription to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationDescription":
        """Create EndToEndTransformationDescription from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndTransformationDescription instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndTransformationDescription since parent returns ARObject
        return cast("EndToEndTransformationDescription", obj)


class EndToEndTransformationDescriptionBuilder:
    """Builder for EndToEndTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationDescription = EndToEndTransformationDescription()

    def build(self) -> EndToEndTransformationDescription:
        """Build and return EndToEndTransformationDescription object.

        Returns:
            EndToEndTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
