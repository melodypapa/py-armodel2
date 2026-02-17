"""EndToEndTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 806)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "clear_from_valid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # clearFromValid
        "counter_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # counterOffset
        "crc_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcOffset
        "data_id_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataIdModeEnum,
        ),  # dataIdMode
        "data_id_nibble": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataIdNibble
        "e2e_profile": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=E2EProfileCompatibilityProps,
        ),  # e2eProfile
        "max_delta": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDelta
        "max_error_state": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxErrorState
        "max_no_new_or": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNoNewOr
        "min_ok_state_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minOkStateInit
        "min_ok_state": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minOkState
        "offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offset
        "profile_behavior_behavior_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EndToEndProfileBehaviorEnum,
        ),  # profileBehaviorBehaviorEnum
        "profile_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # profileName
        "sync_counter_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncCounterInit
        "upper_header": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperHeader
        "window_size_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # windowSizeInit
        "window_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # windowSize
    }

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
