"""CanControllerXlConfigurationRequirements AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)


class CanControllerXlConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerXlConfigurationRequirements."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "error_signaling": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # errorSignaling
        "max_number_of_time_quanta_per": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IntegerBit),
        ),  # maxNumberOfTimeQuantaPer
        "max_pwm_l": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxPwmL
        "max_pwm_o": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxPwmO
        "max_pwm_s": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxPwmS
        "max_sample": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSample
        "max_sync_jump": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSyncJump
        "max_trcv_delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxTrcvDelay
        "min_number_of_time_quanta_per": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IntegerBit),
        ),  # minNumberOfTimeQuantaPer
        "min_pwm_l": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minPwmL
        "min_pwm_o": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minPwmO
        "min_pwm_s": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minPwmS
        "min_sample_point": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minSamplePoint
        "min_sync_jump": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minSyncJump
        "min_trcv_delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minTrcvDelay
        "trcv_pwm_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # trcvPwmMode
    }

    def __init__(self) -> None:
        """Initialize CanControllerXlConfigurationRequirements."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_pwm_l: Optional[PositiveInteger] = None
        self.max_pwm_o: Optional[PositiveInteger] = None
        self.max_pwm_s: Optional[PositiveInteger] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_pwm_l: Optional[PositiveInteger] = None
        self.min_pwm_o: Optional[PositiveInteger] = None
        self.min_pwm_s: Optional[PositiveInteger] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.trcv_pwm_mode: Optional[Boolean] = None


class CanControllerXlConfigurationRequirementsBuilder:
    """Builder for CanControllerXlConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfigurationRequirements = CanControllerXlConfigurationRequirements()

    def build(self) -> CanControllerXlConfigurationRequirements:
        """Build and return CanControllerXlConfigurationRequirements object.

        Returns:
            CanControllerXlConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
