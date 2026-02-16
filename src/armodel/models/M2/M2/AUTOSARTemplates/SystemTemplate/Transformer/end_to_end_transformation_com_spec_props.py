"""EndToEndTransformationComSpecProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "clear_from_valid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # clearFromValid
        "disable_end_to": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # disableEndTo
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
        "sync_counter_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncCounterInit
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
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None


class EndToEndTransformationComSpecPropsBuilder:
    """Builder for EndToEndTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()

    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return EndToEndTransformationComSpecProps object.

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
